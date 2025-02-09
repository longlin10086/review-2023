flag = 0
markdown = """# review-2023

写好了吗？写好了快交。AI 写的不算数哦。

- 2022 年的年终总结见：[saveweb/review-2022](https://github.com/saveweb/review-2022)

保持传统，本项目将长期维护（直到2025年初）。

**想要添加您的年终总结？请发 Issue 或编辑 metadata.md 发PR（不需要填写博客ID）。**

---

"""

with open('metadata.md', 'r') as f:
  lines = f.read().splitlines()

header = lines[0:2]

lines = set(lines[2:])
lines.discard('')
lines = list(lines)
lines.sort()

# with open('metadata.md', 'w') as f:
#   for line in header:
#     f.write(line+'\n')    
#   for line in lines:
#     f.write(line+'\n')

with open('README.md', 'w') as f:
  f.write(markdown+'计数: '+str(len(lines))+' 篇。\n\n')
  f.write('\n'.join(header))
  f.write('\n')
  f.write('\n'.join(set(lines)))