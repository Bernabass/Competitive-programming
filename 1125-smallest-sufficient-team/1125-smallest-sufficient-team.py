class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        required = { s:(1<<i) for i,s in enumerate(req_skills) }
        
        def skillsToBits(skills):
            bits = 0
            for s in skills:
                bits |= required.get(s,0)
            return bits
        
        for i in range(len(people)):
            people[i] = skillsToBits(people[i])


        @cache
        def doit(i, needed):

            if needed == 0: 
                return ()
            
            if i == len(people):
                return None
            
            z = doit(i+1,needed)
            if people[i] & needed:
                zz = doit(i+1, needed & ~people[i])
                if zz is not None:
                    zz = (i,) + zz
                    if z is None or len(zz) < len(z):
                        z = zz
            return z
        
        return doit(0, skillsToBits(req_skills))