1. How to optimize the solution
   1. Metric to optimize: steps (length of the solution string for example)
   2. My optimization ideas:
      1. Sort the inputs by distance from the source (0, 0).
      2. Follow this sorted order.

2. How to get the Pizzabot back to the origin?

3. How to create a solution checker?
   1. split the solution into paths, maybe removing de DROP
      1. If there is a start drop I add a '' (empty string) to the begging.
      2. If there is an extra drop in the same coord I add a '' to the path.
      3. We can improve the empty string if necessary.
   2. Check if the paths have the same elements, not necessary in the same order.
      1. I used Counter for this.