class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # add the largest position to stack 
        # place the two arrays into pairs using zip, sort the array of pairs
        # then we want calculate the time each car will hit the target 
        # if the car behind is faster then the car in front then they become a fleet, then we dont have 
        # to worry about finding all positions because 1 car is only as fast as the car in front of it
        pair  = [[p,s] for p, s in zip(position, speed)]
        pair.sort()
        stack = []

        for p, s in pair[::-1]:
            time = (target - p)/s
            if stack:
                if time <= stack[-1]:
                    continue
                else:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)
                




        #time  = (target - position)/speed

