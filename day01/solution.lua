-- Calorie counting

io.input("./input.txt")

local rations = {}
local elf = {}
for line in io.lines() do
  if line ~= "\n" then
    table.insert(elf, tonumber(line))
    print("Add food to elf")
  else
    table.insert(rations, elf)
    print("Add elf to list and reset elf")
    elf = {}
  end
end

for k, v in ipairs(rations) do
  print(v)
end
