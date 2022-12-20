local score_round = function(left, right)
  -- returns the score of `right`
  -- rock = 1
  -- paper = 2
  -- scissors = 3
  local loss = 0
  local draw = 3
  local win = 6

  if left == right then -- tie
    return right + draw
  elseif (right - left == 1) or (right - left == -2) then -- win
    return right + win
  else -- loss
    return right + loss
  end
end

io.input("./input.txt")

local symbol_map = {
  A=1,
  B=2,
  C=3,
  X=1,
  Y=2,
  Z=3,
}

local total = 0
for round in io.lines() do
  print(round)
  local opp = symbol_map[string.sub(round, 1, 1)]
  local you = symbol_map[string.sub(round, 3, 3)]
  total = total + score_round(opp, you)
end

print(total)
