-- Author: James Barney
-- /u/cardstocks
-- 8-DEC-2013
-- Version 0.1

-- gps.lua   (should probably be called topograph.lua or something, technically)

--[[
Root idea from /u/MonaLot 
--see http://www.reddit.com/r/starbound/comments/1saute/thought_this_would_be_a_cool_idea_for_a_map/
for more information.

So here's my idea/code for a GPS/cartographer tech for Starbound. The idea is that 
when the tech is activated by pressing 'f' on the keyboard, the script takes note
of the character's current position and stores it in the data.map table. As the 
player explores the planet's surface, more and more points are recorded. The final
product would be a graph of some sort that connects the consecutive points in 
the table. Obviously the slope of the line between two points would be the average
change in elevation for the planet over the interval that the player travelled.
This graph could then be stored (or actively displayed!) in a map window
in the UI for each planet and be used for navigation and exploration later.

By continuing to press 'f' and activating the tech, the player will 
effectively be 'mapping' the planet's surface by recording his/her position
as they move around the world. This will work since there is (v. Irritated Koala) 
only one insertion position for each planet from a player's ship. Any "back and
forth" that the player makes will just be recorded as subsequent lines on the map. 
It'll be difficult to break this since right now there is no way to teleport around 
the map and you can only have one tech active at any one point.
Death might be an issue, since the player will appear at the beginning without 
traversing any previous points. 

Anyways, this is as much as I can figure out without an API to work with. You can add 
and 'use' the tech in-game, but nothing that I'm aware of happens. I figured
that someone out there might be able to offer more insight!

Let me know!
]]

function init()
  data.active = false
  data.starterPosition = tech.position() --maybe this should be down further, like in update()?
  data.map = {} --the table for storing the points
  table.insert(data.map, data.starterPosition)
end

function uninit()
  if data.active then
    tech.setParentOffset({0, 0})
    data.active = false
    tech.setVisible(false)
    tech.setParentAppearance("normal")
    tech.setToolUsageSuppressed(false)
    tech.setParentFacingDirection(nil)
  end
end

function input(args)
  if args.moves["special"] == 1 then --when the player presses 'f'
      return "gpsActivate"
    end

  return nil
end

function update(args)
  local curPosition = nil
  if args.actions["gpsActivate"] then
    curPosition = tech.position() --gets the current position
	table.insert(data.map, curPosition) --stores the current position
	data.active = true
  end
  return 0
  -- I'm not sure how to use the data.map table in a window or even print it out in game.
end
