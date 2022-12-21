-- Day 2: Rock Paper Scissors
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
  local opp = symbol_map[string.sub(round, 1, 1)]
  local you = symbol_map[string.sub(round, 3, 3)]
  total = total + score_round(opp, you)
end

print(total)

-- part 2
-- X = lose
-- Y = draw
-- Z = win

local pick_correct_shape = function(left, right)
  if right == "X" then -- lose
    return (symbol_map[left] - 2) % 3 + 1
  elseif right == "Y" then -- draw
    return symbol_map[left]
  else -- win
    return symbol_map[left] % 3 + 1
  end
end

local total2 = 0

io.input("./input.txt")
for round in io.lines() do
  print(round)
  local opp_letter = string.sub(round, 1, 1)
  local you_letter = string.sub(round, 3, 3)
  local opp = symbol_map[opp_letter]
  local your_pick = pick_correct_shape(opp_letter, you_letter)
  total2 = total2 + score_round(opp, your_pick)
end

print(total2)
