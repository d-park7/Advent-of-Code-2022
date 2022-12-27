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
    if string.match(crate, "%a") then -- crate contains alphabet, exclude last numbers
      -- print("insert crate "..crate.." to stack "..stack_num)
      table.insert(stacks[stack_num], 1, crate)
    end
    stack_num = stack_num + 1
  end
  return stacks
end

local function pretty_print_stacks(stacks)
  local max_stack_height = 0
  for i=1,#stacks do
    local h = #stacks[i]
    if max_stack_height < h then
      max_stack_height = h
    end
  end

  print("Stack:")
  for j=max_stack_height,1,-1 do
    local row = {}
    for _, v in ipairs(stacks) do
      if j <= #v then
        table.insert(row, "["..v[j].."]")
      else
        table.insert(row, "   ")
      end
    end
    print(table.concat(row, " "))
  end
end

local function move_crate (line, stacks, verbose, cratemover)
  local move = {}
  for number in string.gmatch(line, "%d+") do -- find numbers in line
    table.insert(move, tonumber(number))
  end
  local n_crates, from, to = table.unpack(move)
  print("move", n_crates, "crates", "from", from, "to", to)
  for i=1,n_crates do
    if cratemover == 9000 then
      table.insert(stacks[to], table.remove(stacks[from]))
    elseif cratemover == 9001 then
      table.insert(stacks[to], #stacks[to]+2-i, table.remove(stacks[from]))
    end
  end
  if verbose then
    pretty_print_stacks(stacks)
  end
  return stacks
end

local function main (filename, cratemover)
  io.input(filename)
  local stacks = {}
  print("Starting stacks")
  for line in io.lines() do
    if string.match(line, "^m") then  -- line starts with "m"
      stacks = move_crate(line, stacks, true, cratemover)
      -- move block
    elseif string.match(line, "%w") then -- line contains alphanumeric
      print(line)
      stacks = parse_starting_stacks(line, stacks)
    else
      pretty_print_stacks(stacks)
    end
  end

  -- print top of each stacks
  for i=1,#stacks do
    local len = #stacks[i]
    print(stacks[i][len])
  end

end

--main("input.txt", 9000)

main("input.txt", 9001)
