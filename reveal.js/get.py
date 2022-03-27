
# read ../presentation/AutoDiff.json and parse it
import json
import sys

with open('../presentation/AutoDiff.json', 'r') as f:
    data = json.load(f)
    
# for each file from files list
# add "<section data-transition="none"><video data-autoplay src="../[FILE]"></video></section>" to a list
# remove ./ at start of file name
# add to output
output = []
for file in data['files']:
    output.append('<section data-transition="none"><video data-autoplay src="../' + file[2:] + '"></video></section>')
    
print('\n'.join(output))
# write output to file vids.html
with open('vids.html', 'w') as f:
    f.write('\n'.join(output))