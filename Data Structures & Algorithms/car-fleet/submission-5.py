class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # # contiguous
        # #posiiton, speed arrays

        # stack = []
        # pairs = [(p, s) for p, s in zip(position, speed)]
        # pairs.sort(reverse=True)

        # stack.append(target - pairs[0][0] / pairs[0][1])
        # for (p,s) in pairs:
        #     time = (target - p) / s
        #     stack.append(time)
        #     if (len(stack) >= 2 and stack[-2] >= stack[-1]):
        #         stack.pop()
        # return len(stack)


        cars = [(p,s) for p,s in zip(position, speed)]
        cars.sort(reverse=True)
        numfleets = 1
        nearestfleet = (target - cars[0][0]) / cars[0][1]
        # print(cars)
        for car in cars:
            time = (target - car[0] )/ car[1]
            # print(time)
            print(nearestfleet)
            if (time > nearestfleet):
                # print(" reac÷hed if ")
                nearestfleet = time
                numfleets += 1
        return numfleets

            # if cars[l + 1][1] > cars[l][1]:
            #     time = (cars[l][0] - cars[l + 1][0]) / cars[l+1][1]
            #     if (target - cars[l][0]) / cars[l][1] <= time:





        