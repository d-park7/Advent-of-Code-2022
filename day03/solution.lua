-- Day 3: Rucksack Reorganization 
-- a-z have priorities 1-26
-- A-Z have priorities 27-52

local alphabet = "abcdefghijklmnopqrstuvwxyz"

local item_priority = {}
local priority = 1
for letter in string.gmatch(alphabet..string.upper(alphabet), ".") do
  item_priority[letter] = priority
  priority = priority + 1
end

local function split_rucksack (rucksack)
  local mid = string.len(rucksack) // 2
  local compartment1 = string.sub(rucksack, 1, mid)
  local compartment2 = string.sub(rucksack, mid + 1)
  -- print("rucksack", rucksack, compartment1, compartment2)
  return compartment1, compartment2
end

local function find_duplicate_item (comp1, comp2)
  local n = string.len(comp1)
  for i = 1,n do
    local letter = string.sub(comp1, i, i)
    if string.find(comp2, letter) ~= nil then
      return letter
    end
  end
  print("No duplicates found.")
end

local function part_one (filename)
  io.input(filename)
  local total_priority = 0
  for line in io.lines() do
    local c1, c2 = split_rucksack(line)
    local dup = find_duplicate_item(c1, c2)
    total_priority = total_priority + item_priority[dup]
  end
  return total_priority
end

local function find_badge (r1, r2, r3)
  local matches = {}
  for item1 in string.gmatch(r1, ".") do
    for item2 in string.gmatch(r2, ".") do
      if item1 == item2 then
        for item3 in string.gmatch(r3, ".") do
          if item1 == item3 then
            return item1
          end
        end
      end
    end
  end
  print("Badge not found.")
end

local function part_two (filename)
  io.input(filename)
  local total_priority = 0
  local group_of_three = {}
  local count = 0
  for line in io.lines() do
    table.insert(group_of_three, line)
    count = count + 1
    if count % 3 == 0 then -- find badge and reset group
      local badge = find_badge(table.unpack(group_of_three))
      print("badge:", badge)
      total_priority = total_priority + item_priority[badge]
      group_of_three = {}
    end
  end
  return total_priority
end

print(part_one("input.txt"))

print(part_two("input.txt"))
