class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        occurence = defaultdict(int)
        res = []
        for cp_dom in cpdomains:
            cp_dom = cp_dom.split()
            rep , sub_dom = int(cp_dom[0]) , cp_dom[1].split(".")
            count = 0
            while count < len(sub_dom):
                occurence[".".join(sub_dom[count:])] += rep
                count += 1
        for key , val in occurence.items():
            res.append(" ".join([str(val),key]))
        return res