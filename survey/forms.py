from django import forms

class SurveyForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Enter your full name"}),
    )
    number = forms.CharField(
        label="Phone_Number",
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Enter your phone number"}),
    )
    email = forms.EmailField(
        label="Gmail",
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email address"}),
    )
    unit = forms.CharField(
        label="Unit (Optional)",
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Enter unit (if applicable)"}),
    )
    CHOICES = [
        (0, "0 - Not at all"),
        (1, "1 - Sometimes"),
        (2, "2 - Often"),
        (3, "3 - Almost always"),
    ]

    Q1 = forms.ChoiceField(
        choices=CHOICES,
        label="1. I found it hard to wind down",
        widget=forms.RadioSelect,
    )
    Q2 = forms.ChoiceField(
        choices=CHOICES,
        label="2. I was aware of dryness of my mouth",
        widget=forms.RadioSelect,
    )
    Q3 = forms.ChoiceField(
        choices=CHOICES,
        label="3. I couldn’t seem to experience any positive feeling at all",
        widget=forms.RadioSelect,
    )
    Q4 = forms.ChoiceField(
        choices=CHOICES,
        label="4. I experienced breathing difficulty (e.g. excessively rapid breathing, breathlessness in the absence of physical exertion)",
        widget=forms.RadioSelect,
    )
    Q5 = forms.ChoiceField(
        choices=CHOICES,
        label="5. I found it difficult to work up the initiative to do things",
        widget=forms.RadioSelect,
    )
    Q6 = forms.ChoiceField(
        choices=CHOICES,
        label="6. I tended to over-react to situations",
        widget=forms.RadioSelect,
    )
    Q7 = forms.ChoiceField(
        choices=CHOICES,
        label="7. I experienced trembling (e.g. in the hands)",
        widget=forms.RadioSelect,
    )
    Q8 = forms.ChoiceField(
        choices=CHOICES,
        label="8. I felt that I was using a lot of nervous energy",
        widget=forms.RadioSelect,
    )
    Q9 = forms.ChoiceField(
        choices=CHOICES,
        label="9. I was worried about situations in which I might panic and make a fool of myself",
        widget=forms.RadioSelect,
    )
    Q10 = forms.ChoiceField(
        choices=CHOICES,
        label="10. I felt that I had nothing to look forward to",
        widget=forms.RadioSelect,
    )
    Q11 = forms.ChoiceField(
        choices=CHOICES,
        label="11. I found myself getting agitated",
        widget=forms.RadioSelect,
    )
    Q12 = forms.ChoiceField(
        choices=CHOICES,
        label="12. I found it difficult to relax",
        widget=forms.RadioSelect,
    )
    Q13 = forms.ChoiceField(
        choices=CHOICES,
        label="13. I felt down-hearted and blue",
        widget=forms.RadioSelect,
    )
    Q14 = forms.ChoiceField(
        choices=CHOICES,
        label="14. I was intolerant of anything that kept me from getting on with what I was doing",
        widget=forms.RadioSelect,
    )
    Q15 = forms.ChoiceField(
        choices=CHOICES,
        label="15. I felt I was close to panic",
        widget=forms.RadioSelect,
    )
    Q16 = forms.ChoiceField(
        choices=CHOICES,
        label="16. I was unable to become enthusiastic about anything",
        widget=forms.RadioSelect,
    )
    Q17 = forms.ChoiceField(
        choices=CHOICES,
        label="17. I felt I wasn’t worth much as a person",
        widget=forms.RadioSelect,
    )
    Q18 = forms.ChoiceField(
        choices=CHOICES,
        label="18. I felt that I was rather touchy",
        widget=forms.RadioSelect,
    )
    Q19 = forms.ChoiceField(
        choices=CHOICES,
        label="19. I was aware of the action of my heart in the absence of physical exertion (e.g. sense of heart rate increase, heart missing a beat)",
        widget=forms.RadioSelect,
    )
    Q20 = forms.ChoiceField(
        choices=CHOICES,
        label="20. I felt scared without any good reason",
        widget=forms.RadioSelect,
    )
    Q21 = forms.ChoiceField(
        choices=CHOICES,
        label="21. I felt that life was meaningless",
        widget=forms.RadioSelect,
    )   