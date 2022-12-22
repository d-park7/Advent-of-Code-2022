-- Day 5: Supply Stacks

local function parse_starting_stacks (line, stacks)
  local n = #line
  local num_cols = (n + 1) / 4

  -- initialize all stacks
  if #stacks == 0 then
    for _=1,num_cols do
      table.insert(stacks, {})
    end
  end

  -- Loop through crates in a line
  local stack_num = 1
  for i = 2, n, 4 do
    local crate = string.sub(line, i, i)
    -- print("crate: "..crate)
    -- print("stack num: "..stack_num)
    if string.match(crate, "%a") then
      -- print("insert crate "..crate.." to stack "..stack_num)
      table.insert(stacks[stack_num], 1, crate)
    end
    stack_num = stack_num + 1
  end
  return stacks
end

local function move_crate (line)
  local move = {}
  for number in string.gmatch(line, "%d+") do
    table.insert(move, tonumber(number))
  end
  local n_crates, from, to = table.unpack(move)
  print("move", n_crates, "crates", "from", from, "to", to)
end

local function print_stacks(stacks)
  local max_stack_height = 0
  for i=1,#stacks do
    local h = #stacks[i]
    if max_stack_height < h then
      max_stack_height = h
    end
  end

  for j=max_stack_height,1,-1 do
    local row = {}
    for k, v in ipairs(stacks) do
      if j <= #v then
        table.insert(row, "["..v[j].."]")
      else
        table.insert(row, "   ")
      end
    end
    print(table.concat(row, " "))
  end
end

local function part_one (filename)
  io.input(filename)
  local stacks = {}
  print("Starting stacks")
  for line in io.lines() do
    if string.match(line, "^m") then
      move_crate(line)
      -- move block
    elseif string.match(line, "%w") then
      print(line)
      stacks = parse_starting_stacks(line, stacks)
    else
      print_stacks(stacks)
    end
  end
end

part_one("testinput.txt")
