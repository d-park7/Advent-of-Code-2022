-- Day 4: Camp Cleanup
--
-- 2-4,6-8

local function is_completely_overlapped (r1, r2)
  if ((r1.left <= r2.left) and (r2.right <= r1.right)) then
    return true
  elseif ((r2.left <= r1.left) and (r1.right <= r2.right)) then
    return true
  else
    return false
  end
end

local function is_overlapped (r1, r2)
  return math.max(r1.left, r2.left) <= math.min(r1.right, r2.right)
end

local function part_one_and_two (filename)
  io.input(filename)

  local total_overlaps = 0
  local total_complete_overlaps = 0
  local total_pairs = 0
  local elf1 = {}
  local elf2 = {}
  for line in io.lines() do
    local t = {}
    for number in string.gmatch(line, "%d+") do
      table.insert(t, tonumber(number))
    end
    if #t ~= 4 then
      print("Incorrect t size:", #t)
    end
    elf1.left, elf1.right, elf2.left, elf2.right = table.unpack(t)
    if is_overlapped(elf1, elf2) then
      total_overlaps = total_overlaps + 1
      if is_completely_overlapped(elf1, elf2) then
        total_complete_overlaps = total_complete_overlaps + 1
      end
    end
    total_pairs = total_pairs + 1
  end
  print("total overlaps", total_overlaps)
  print("total complete overlaps", total_complete_overlaps)
end


part_one_and_two("input.txt")
