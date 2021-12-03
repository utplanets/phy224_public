import sys, json, yaml

input_fname = sys.argv[1]
output_fname = sys.argv[2]

x = "".join(open(input_fname,'r').readlines())
p = slice(3,x[3:].index("---")+3)
print(x[p])
y=yaml.safe_load(x[p])
z = json.load(open(output_fname,'r'))
z["metadata"]["jekyll"] = y
json.dump(z,open(output_fname,'w'),indent=2)
