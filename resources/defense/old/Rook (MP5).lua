EnablePrimaryMouseButtonEvents(true);
 
function OnEvent(event, arg)
	if IsKeyLockOn("capslock" )then
		if IsMouseButtonPressed(3)then
			repeat	
				if IsMouseButtonPressed(1) then
					repeat
						MoveMouseRelative(-1,17)
						Sleep(25)
					until not IsMouseButtonPressed(1)
				end				
			until not IsMouseButtonPressed(3)
		end		
	end
end