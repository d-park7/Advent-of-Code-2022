-- Calorie counting
print("Run file")
io.input("./input.txt")

local rations = {}
local elf = {}

for line in io.lines() do
  -- print("The line is", line)
  if string.match(line, "^%w") then
    table.insert(elf, line)
    -- print("Add food to elf")
  else
    table.insert(rations, elf)
    -- print("Add elf to list and reset elf")
    elf = {}
  end
end
table.insert(rations, elf)
-- print("Add last elf to list")

-- print("Loop ended")
local totals = {}
for k, e in ipairs(rations) do
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
