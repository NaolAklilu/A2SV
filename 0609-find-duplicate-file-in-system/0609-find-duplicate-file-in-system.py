class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dic = defaultdict(list)
        ans = []
        for path in paths:
            cur_path = list(path.split(" "))
            for file in cur_path[1:]:
                string = file.split("(")
                file_name = string[0]
                content = string[1][:-1]
                
                path_dic[content].append(cur_path[0] + "/" + file_name)
         
        ans = []
        for path in path_dic.values():
            if len(path) > 1:
                ans.append(path)
                
        return ans
                
               