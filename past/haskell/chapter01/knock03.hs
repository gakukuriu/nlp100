import Text.Regex

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

main = print [length w | w <- words (subRegex (mkRegex "[,.]") s "")]
