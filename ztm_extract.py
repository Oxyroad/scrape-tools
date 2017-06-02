import re


def extract(ztm_file, output_csv):
    # stolen from https://github.com/javnik36/ZTMvsOSM and modified a bit
    inp = open(ztm_file, 'r', encoding="windows-1250")
    out = open(output_csv, 'w')

    x_lines = list()
    x_should_go = False
    x_station = ''
    for line in inp:
        pattern = "^\s+(\d{6}).{94}\Y=\s(\d{2}\.\d{6})\s+\X=\s(\d{2}\.\d{6})"
        pattern_match = re.search(pattern, line)
        x_station_find = re.findall('^   \d{4}   ([^,]+),', line)
        if x_station_find:
            x_station = x_station_find[0]

        if pattern_match:
            if x_should_go:
                out.write(',' + '|'.join(list(set(x_lines))) + '\n')
                x_lines = list()
            out.write(','.join([pattern_match.group(3), pattern_match.group(2), x_station]))
            x_should_go = True
        else:
            if x_should_go:
                x_mine = [str(int(x)) for x in re.findall('\d+', line[line.find(':')+1:].strip()) if 0 < int(x) < 50]
                x_lines.extend(x_mine)
    if x_should_go:
        out.write('|'.join(list(set(x_lines))))
        out.write("\n")

    inp.close()
    out.close()
