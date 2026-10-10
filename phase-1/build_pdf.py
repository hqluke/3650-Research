#!/usr/bin/env python3
"""Build Phase1_Usability_Audit.pdf from Phase1_Usability_Audit.md.

Needs `pip install markdown pikepdf` and Google Chrome or Chromium.
Run: python build_pdf.py

Chrome prints a tagged PDF (headings, lists, tables, figures with alt text,
bookmarks from the headings). pikepdf then sets the viewer and metadata flags
that Chrome leaves out.
"""
import html
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import markdown
import pikepdf
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

HERE = Path(__file__).resolve().parent
SRC = HERE / "Phase1_Usability_Audit.md"
OUT = HERE / "Phase1_Usability_Audit.pdf"
TITLE = "Phase 1: Contextual Research & Diagnostic Usability Audit"
AUTHOR = "Luke Peterson"
CALLOUT = re.compile(r"\[!(\w+)\]\s*([^\n]*)\n?")
ID_IN_TEXT = re.compile(r"\b[A-Z]-\d\d\b")
SHORT_ID = re.compile(r"[A-Z]{1,2}-?\d+(, [A-Z]{1,2}-?\d+)*")

CSS = """
@page {
  size: Letter;
  margin: 0.75in 0.8in 0.85in;
  @bottom-center { content: "Page " counter(page) " of " counter(pages); font: 9pt "Noto Sans", sans-serif; color: #444; }
}
html { font-family: "Noto Sans", "Liberation Sans", sans-serif; font-size: 10.5pt; line-height: 1.5; color: #1a1a1a; }
body { margin: 0; }
h1, h2, h3, h4 { color: #12324f; line-height: 1.25; break-after: avoid; break-inside: avoid; }
h1 { font-size: 21pt; margin: 0 0 4pt; }
h1 + p { font-size: 12pt; margin-bottom: 2pt; }
h1 + p + p { margin-bottom: 0; }
h2 { font-size: 15pt; margin: 22pt 0 8pt; padding-bottom: 3pt; border-bottom: 1.5pt solid #12324f; }
h3 { font-size: 12.5pt; margin: 16pt 0 6pt; }
h4 { font-size: 11pt; margin: 12pt 0 4pt; }
p, li { orphans: 3; widows: 3; }
p { margin: 0 0 7pt; }
ul, ol { margin: 0 0 8pt; padding-left: 18pt; }
li { margin-bottom: 2pt; }
a { color: #0b5394; }
code { font-family: "Liberation Mono", monospace; font-size: 0.86em; background: #eef1f4; padding: 0 1pt; border-radius: 2pt; }
table { width: 100%; border-collapse: collapse; margin: 6pt 0 12pt; font-size: 9pt; line-height: 1.35; }
th, td { border: 0.75pt solid #8d99a6; padding: 3pt 5pt; text-align: left; vertical-align: top; }
thead th { background: #e3e9ef; }
tbody th { background: #f3f5f7; }
table, tr { break-inside: avoid; }
p:has(+ table) { break-after: avoid; }
table.matrix { font-size: 8.5pt; }
table.matrix td, table.matrix th { padding: 2.5pt 3pt; }
figure { margin: 10pt 0 14pt; break-inside: avoid; }
figure { border: 0.75pt solid #8d99a6; padding: 6pt 6pt 2pt; }
figure img { display: block; max-width: 100%; max-height: 4.6in; margin: 0 auto; }
.nowrap { white-space: nowrap; }
h2:last-of-type ~ p { font-size: 9.5pt; padding-left: 0.4in; text-indent: -0.4in; margin-bottom: 5pt; }
figcaption { font-size: 9pt; margin-top: 4pt; color: #333; }
.callout { margin: 8pt 0 12pt; padding: 7pt 11pt 2pt; border-left: 4pt solid; border-radius: 0 3pt 3pt 0; break-inside: avoid; }
.callout-title { font-weight: 700; margin-bottom: 3pt; }
.summary { border-color: #1f5f99; background: #eef4fa; }
.summary .callout-title { color: #174a78; }
.important { border-color: #6a3d9a; background: #f4effa; }
.important .callout-title { color: #4f2c75; }
.warning { border-color: #b35900; background: #fdf3e7; }
.warning .callout-title { color: #7f3f00; }
.quote { border-color: #5b6770; background: #f4f5f6; }
.quote .callout-title { color: #3d464d; }
"""


class ReportTree(Treeprocessor):
    """Turn Obsidian callouts, image + caption pairs, and tables into accessible HTML."""

    def run(self, root):
        for parent in list(root.iter()):
            kids = list(parent)
            for i, el in enumerate(kids):
                if el.tag == "blockquote":
                    for bq in self.split_callouts(el, parent):
                        self.callout(bq)
                elif el.tag == "table":
                    self.table(el)
                elif el.tag == "code" and "/" in (el.text or ""):
                    self.break_after_slashes(el)
                elif el.tag == "p" and len(el) == 1 and el[0].tag == "img" and not (el.text or "").strip():
                    nxt = kids[i + 1] if i + 1 < len(kids) else None
                    self.figure(el, nxt, parent)

    def split_callouts(self, bq, parent):
        """Markdown merges back-to-back callouts into one blockquote. Split them apart again."""
        out = [bq]
        for child in list(bq)[1:]:
            if child.tag == "p" and CALLOUT.match(child.text or ""):
                new = ET.Element("blockquote")
                parent.insert(list(parent).index(out[-1]) + 1, new)
                out.append(new)
            if out[-1] is not bq:
                bq.remove(child)
                out[-1].append(child)
        return out

    def callout(self, bq):
        if not len(bq) or bq[0].tag != "p":
            return
        first = bq[0]
        m = CALLOUT.match(first.text or "")
        if not m:
            return
        kind, title = m.group(1).lower(), m.group(2).strip()
        first.text = first.text[m.end():]
        if not first.text.strip() and not len(first):
            bq.remove(first)
        heading = ET.Element("p", {"class": "callout-title"})
        heading.text = title or kind.title()
        bq.insert(0, heading)
        if kind == "quote":
            bq.set("class", "callout quote")
        else:
            bq.tag = "div"
            bq.set("class", f"callout {kind}")
            bq.set("role", "note")
            bq.set("aria-label", heading.text)

    def break_after_slashes(self, code):
        """Let long paths wrap at a slash instead of mid-number."""
        parts = code.text.split("/")
        code.text = parts[0] + "/"
        for i, part in enumerate(parts[1:], 1):
            ET.SubElement(code, "wbr").tail = part + ("/" if i < len(parts) - 1 else "")

    def figure(self, p, caption, parent):
        p.tag = "figure"
        if caption is not None and caption.tag == "p" and len(caption) == 1 and caption[0].tag == "em" \
                and (caption[0].text or "").startswith("Figure"):
            em = caption[0]
            cap = ET.SubElement(p, "figcaption")
            cap.text, cap.tail = em.text, None
            for child in list(em):
                cap.append(child)
            parent.remove(caption)

    def table(self, t):
        head = t.find("thead/tr")
        if head is None:
            return
        cells = list(head)
        for th in cells:
            th.set("scope", "col")
        if len(cells) > 6:
            t.set("class", "matrix")
        # A blank top-left header means the first column holds row labels.
        for cell in t.iter():
            if cell.tag not in ("td", "th"):
                continue
            text = "".join(cell.itertext()).strip()
            if not text and not len(cell):
                cell.text = "\u00a0"  # Chrome drops empty cells from the tag tree, which misaligns columns
            elif SHORT_ID.fullmatch(text):
                cell.set("class", "nowrap")
        if not "".join(cells[0].itertext()).strip(" \u00a0"):
            cells[0].tag = "td"
            cells[0].attrib.pop("scope")
            for row in t.findall("tbody/tr"):
                if "".join(row[0].itertext()).strip():
                    row[0].tag = "th"
                    row[0].set("scope", "row")


class ReportExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(ReportTree(md), "report", 5)


def build_html():
    body = markdown.markdown(SRC.read_text(), extensions=["tables", "sane_lists", ReportExtension()])
    # Keep IDs like H-01 from splitting at the hyphen. Only touches text between tags.
    body = re.sub(r">[^<]+<", lambda m: ID_IN_TEXT.sub(r'<span class="nowrap">\g<0></span>', m.group(0)), body)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{TITLE.replace("&", "&amp;")}</title>
<base href="{HERE.as_uri()}/">
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""


def print_pdf(html_path, pdf_path):
    chrome = next(filter(None, map(shutil.which, ["google-chrome-stable", "google-chrome", "chromium"])), None)
    if not chrome:
        raise SystemExit("Google Chrome or Chromium is required")
    subprocess.run([
        chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
        "--export-tagged-pdf", "--generate-pdf-document-outline",
        f"--print-to-pdf={pdf_path}", html_path.as_uri(),
    ], check=True, capture_output=True)


PAINT_OPS = {"Tj", "TJ", "'", '"', "f", "F", "f*", "S", "s", "B", "B*", "b", "b*", "sh", "Do"}


def drop_empty_marked_content(pdf, page, parent_tree):
    """When a heading gets pushed to the next page, Chrome leaves an empty tagged fragment on the
    page before. Screen readers then announce an empty heading. Remove those fragments."""
    ops = list(pikepdf.parse_content_stream(page))
    stack, drop, empty = [], set(), []
    for i, (operands, op) in enumerate(ops):
        name = str(op)
        if name in ("BDC", "BMC"):
            props = operands[1] if name == "BDC" and len(operands) > 1 else None
            mcid = props.get("/MCID") if isinstance(props, pikepdf.Dictionary) else None
            stack.append([i, mcid, False])
        elif name == "EMC" and stack:
            start, mcid, painted = stack.pop()
            if stack:
                stack[-1][2] |= painted
            if mcid is not None and not painted:
                drop.update((start, i))
                empty.append(int(mcid))
        elif name in PAINT_OPS and stack:
            stack[-1][2] = True
    if not empty:
        return
    page.obj.Contents = pdf.make_stream(pikepdf.unparse_content_stream([o for i, o in enumerate(ops) if i not in drop]))
    owners = parent_tree[int(page.obj.StructParents)]
    for mcid in empty:
        elem, target = owners[mcid], mcid
        owners[mcid] = None
        while isinstance(elem, pikepdf.Dictionary):
            kids = elem.get("/K")
            kids = list(kids) if isinstance(kids, pikepdf.Array) else [kids]
            keep = [kid for kid in kids if not refers_to(kid, target, elem, page)]
            if keep:
                elem.K = pikepdf.Array(keep)
                break
            elem, target = elem.get("/P"), elem  # now empty, so remove it from its parent too


def refers_to(kid, target, elem, page):
    """Does this /K entry of elem point at target (an MCID on this page, or a child element)?"""
    if isinstance(target, pikepdf.Dictionary):
        return isinstance(kid, pikepdf.Dictionary) and kid.objgen == target.objgen
    here = page.obj.objgen
    if isinstance(kid, int):
        return kid == target and elem.get("/Pg", page.obj).objgen == here
    return (isinstance(kid, pikepdf.Dictionary) and kid.get("/MCID") == target
            and kid.get("/Pg", elem.get("/Pg", page.obj)).objgen == here)


def parent_tree_map(tree):
    """Flatten the ParentTree number tree into {StructParents key: array of owners}."""
    found = {}
    def visit(node):
        nums = node.get("/Nums", [])
        for i in range(0, len(nums), 2):
            found[int(nums[i])] = nums[i + 1]
        for kid in node.get("/Kids", []):
            visit(kid)
    visit(tree.ParentTree)
    return found


def mark_artifacts(pdf, page):
    """Wrap untagged text (the page number footer) in /Artifact so every mark is tagged or an artifact."""
    out, block, depth, tagged = [], None, 0, False
    for operands, op in pikepdf.parse_content_stream(page):
        name = str(op)
        if block is None and depth == 0 and name == "BT":
            block, tagged = [], False
        if name in ("BDC", "BMC"):
            depth += 1
            tagged = tagged or block is not None
        elif name == "EMC":
            depth -= 1
        if block is None:
            out.append((operands, op))
            continue
        block.append((operands, op))
        if name == "ET":
            if tagged:
                out += block
            else:
                out += [([pikepdf.Name.Artifact], pikepdf.Operator("BMC")), *block, ([], pikepdf.Operator("EMC"))]
            block = None
    page.obj.Contents = pdf.make_stream(pikepdf.unparse_content_stream(out))


def fix_figures(node):
    """Chrome tags <figure> as a Figure around the image's Figure. Make the outer one a plain group."""
    k = node.get("/K")
    kids = list(k) if isinstance(k, pikepdf.Array) else [k]
    kids = [c for c in kids if isinstance(c, pikepdf.Dictionary) and "/S" in c]
    if node.get("/S") == "/Figure" and "/Alt" not in node and any(c.get("/S") == "/Figure" for c in kids):
        node.S = pikepdf.Name.Div
    for c in kids:
        fix_figures(c)


def add_list_bodies(pdf, node):
    """Chrome puts list item content straight under LI. PDF/UA wants it inside an LBody."""
    kids = node.get("/K")
    kids = list(kids) if isinstance(kids, pikepdf.Array) else [kids]
    elems = [c for c in kids if isinstance(c, pikepdf.Dictionary) and "/S" in c]
    if node.get("/S") == "/LI" and len(elems) == len(kids):
        body = [c for c in elems if c.S != "/Lbl"]
        if body and not any(c.S == "/LBody" for c in body):
            lbody = pdf.make_indirect(pikepdf.Dictionary(Type=pikepdf.Name.StructElem, S=pikepdf.Name.LBody, P=node, K=pikepdf.Array(body)))
            for c in body:
                c.P = lbody
            node.K = pikepdf.Array([c for c in elems if c.S == "/Lbl"] + [lbody])
    for c in elems:
        add_list_bodies(pdf, c)


def fix_outline(pdf, headings):
    """Chrome garbles bookmark titles for headings that start a new page. Use the source headings."""
    with pdf.open_outline() as outline:
        items = []
        def visit(nodes):
            for node in nodes:
                items.append(node)
                visit(node.children)
        visit(outline.root)
        if len(items) != len(headings):
            raise SystemExit(f"outline has {len(items)} entries but the report has {len(headings)} headings")
        for item, title in zip(items, headings):
            item.title = title


def finish_pdf(pdf_path, headings):
    with pikepdf.open(pdf_path, allow_overwriting_input=True) as pdf:
        tree = pdf.Root.StructTreeRoot
        owners = parent_tree_map(tree)
        for page in pdf.pages:
            drop_empty_marked_content(pdf, page, owners)
        fix_outline(pdf, headings)
        # Chrome uses the PDF 2.0 names Strong and Em. Map them to the PDF 1.7 standard type.
        tree.RoleMap = pikepdf.Dictionary(Strong=pikepdf.Name.Span, Em=pikepdf.Name.Span)
        fix_figures(tree)
        add_list_bodies(pdf, tree)
        for page in pdf.pages:
            mark_artifacts(pdf, page)
        root = pdf.Root
        root.Lang = pikepdf.String("en-US")
        root.ViewerPreferences = pikepdf.Dictionary(DisplayDocTitle=True)
        root.PageMode = pikepdf.Name.UseOutlines
        pdf.docinfo["/Title"] = TITLE
        pdf.docinfo["/Author"] = AUTHOR
        with pdf.open_metadata() as meta:
            meta["dc:title"] = TITLE
            meta["dc:creator"] = [AUTHOR]
            meta["dc:language"] = ["en-US"]
            meta["pdfuaid:part"] = "1"
        for page in pdf.pages:
            annots = page.obj.get("/Annots", [])
            if annots:
                page.obj.Tabs = pikepdf.Name.S
            for a in annots:
                if a.get("/Subtype") == "/Link" and "/Contents" not in a:
                    uri = a.get("/A", {}).get("/URI")
                    a.Contents = pikepdf.String(f"Link to {uri}" if uri else "Link")
        pdf.save(pdf_path, min_version="1.7")


def main():
    page = build_html()
    headings = [html.unescape(re.sub(r"<[^>]+>", "", h)).strip() for h in re.findall(r"<h[1-6][^>]*>(.*?)</h[1-6]>", page, re.S)]
    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "report.html"
        html_path.write_text(page)
        print_pdf(html_path, OUT)
    finish_pdf(OUT, headings)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
