from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class VoteTopic(models.Model):
    proposal = models.TextField(help_text="The proposal text")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Proposal by {}: {}".format(self.owner, self.proposal[:100])

    def vote_results(self):
        results = {}
        for i in Vote.VOTE_OPTIONS:
            results[i[1]] = self.votes.filter(vote_value=i[0]).count()
        return results


class Vote(models.Model):
    VOTE_NO = 0
    VOTE_YES = 1
    VOTE_ABS = 2

    VOTE_OPTIONS = [
        [VOTE_YES, "yes"],
        [VOTE_NO, "no"],
        [VOTE_ABS, "abstain"]
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    vote_value = models.IntegerField(choices=VOTE_OPTIONS)

    topic = models.ForeignKey(VoteTopic,
                              on_delete=models.CASCADE,
                              related_name="votes")

    class Meta:
        unique_together = ["owner", "topic"]

    def __str__(self):
        return "{} voted {} for PROPOSAL_ID:{}".format(self.owner,
                                            self.get_vote_value_display(),
                                            self.topic.id)

