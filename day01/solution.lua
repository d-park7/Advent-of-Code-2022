-- Calorie counting
io.input("./input.txt")

local rations = {}
local elf = {}

for line in io.lines() do
  if string.match(line, "^%w") then -- match on alphanumeric character
    table.insert(elf, line)
  else
    table.insert(rations, elf)
    elf = {}
  end
end
table.insert(rations, elf) -- add last elf

local totals = {}
for _, e in ipairs(rations) do
  local total = 0
  for _, r in ipairs(e) do
    total = total + r
  end
  table.insert(totals, total)
end

print("Max elf: ", math.max(table.unpack(totals)))
table.sort(totals)

local t = 0
local n = 3
print("top n=",n)
for i = 1,n do
  print(totals[#totals + 1 - i])
  t = t + totals[#totals + 1 - i]
end
print("top n sum: ", t)
