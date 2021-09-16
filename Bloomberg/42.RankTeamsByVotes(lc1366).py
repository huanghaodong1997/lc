class Solution:
    def rankTeams(self, votes) -> str:
        team_score = {}
        for team in votes[0]:
            team_score[team] = [0] * 26
            
        for vote in votes:
            
            for i, team in enumerate(vote):
                team_score[team][i] -= 1
        sorted_score = sorted([(team_score[team], team) for team in team_score])
        res = [team for _, team in sorted_score]
        return "".join(res)