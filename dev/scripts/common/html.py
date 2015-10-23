class Html():
    
    def write_html(self, tree, html_output, encoding=CODEC):
        html = "<table>\n"
        for entry in tree.getroot():
            lx = entry.findtext('lx')
            ps = entry.findtext('ps')
            ge = entry.findtext('ge')
            html += "  <tr><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (lx, ps, ge)
        html += "</table>"
        output = open_file(html_output, 'w', encoding=encoding)
        output.write(html)
        output.close()
