

session_split = 38
row = []
poster_count = 1
with open('posters.txt') as f:
    for l in f:
        l = l.split('|')
        if len(l) == 1:
            continue
        if l[4] == 'Cognitive':
            col = 'set1'
        elif l[4] == 'Clinical':
            col = 'set2'
        else:
            col = 'set3'

        if len(row) < session_split:
            sess = 'A'
            post_num = poster_count
        else:
            sess = 'B'
            post_num = poster_count - session_split

        row.append( '\cellcolor{%s!50}{\\bf %s-%d} & {\\footnotesize %s} {\\bf\\footnotesize %s~%s}, {\\footnotesize %s}  \\\\\n' % (col,sess, post_num, l[5][:-1], l[1], l[2], l[3] ) )
        poster_count += 1

with open('posters_table.tex','w') as pt:

    pt.write("""\\begin{figure}[htp]
\\centering
\\footnotesize
\\begin{tabularx}{\\textwidth}{lp{.92\linewidth}}
\\multicolumn{2}{l}{\\Large Posters - Day 1 \\hspace{8cm} \\colorbox{set1!50}{\\small\\strut Cognitive}\\colorbox{set2!50}{\\small\\strut Clinical}\\colorbox{set3!50}{\\small\\strut Methods}}\\\\
\\toprule
""")

    for ii in range(session_split):
        pt.write( row[ii] )

    pt.write("""\\bottomrule
\\end{tabularx}
\\end{figure}
""")

with open('posters_table2.tex','w') as pt:

    pt.write("""\\begin{figure}[htp]
\\centering
\\footnotesize
\\begin{tabularx}{\\textwidth}{lp{.92\linewidth}}
\\multicolumn{2}{l}{\\Large Posters - Day 2 \\hspace{8cm} \\colorbox{set1!50}{\\small\\strut Cognitive}\\colorbox{set2!50}{\\small\\strut Clinical}\\colorbox{set3!50}{\\small\\strut Methods}}\\\\
\\toprule
""")

    for ii in range(session_split,len(row)):
        pt.write( row[ii] )

    pt.write("""\\bottomrule
\\end{tabularx}
\\end{figure}
""")
