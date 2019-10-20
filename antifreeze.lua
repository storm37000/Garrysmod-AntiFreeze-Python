local port = string.Split(game.GetIPAddress(),":")[2]

timer.Create( "antifreeze", 1, 0, function()
  file.Write( "antifreeze/time_" .. port .. ".txt", os.time() )
end)
