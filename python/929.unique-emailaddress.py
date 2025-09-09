class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cnt = 0
        eset = set()
        for e in emails:
            local, domain = e.split("@", 1)
            userName = local.split("+")[0].replace(".", "")
            sendTo = userName + "@" + domain
            eset.add(sendTo)

        return len(eset)
