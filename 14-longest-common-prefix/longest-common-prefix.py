class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # İlk stringi prefix olarak al
        prefix = strs[0]
        
        # Diğer stringlerle karşılaştır
        for s in strs[1:]:
            # prefix s'in başında yoksa kısalt
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix