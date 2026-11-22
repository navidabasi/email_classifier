def classify_email(subject: str, body: str) -> list[str]:
    """
    considering our email data has 4 columns: id, subject, body, label, we dont need id, and ofc we dont need label, so we only use subject and body
    the function takes both, process them and then returns the label of the email as: confirmation, booking_inquiry, booking_follow_up, unrelated
    """

    # cleaning data making it all lower case and removing any spaces from either side of the text
    subject = subject.lower().strip()
    body = body.lower().strip()

    # considering the subject usually gives the reason of contact, we first need to analyze the subject
    # then we analyze the body, for this case we do a two step at once move, concating both into one string and then analyzing it.

    email_content = subject + " " + body # a space is necessary to avoid unwanted changes on the text

    # considering this is a dummy check we create 3 different list of keywords for each label, else it would be unrelated.

    confirmation_keywords = [
    "i confirm",
    "we accept",
    "please finalize"
        ]   
    booking_inquiry_keywords = [
    "availability",
    "available",
    "price",
    "how much"
        ]
    booking_follow_up_keywords = [
        "reschedule",
        "cancel",
        "refund",
        "resend",
        "invoice",
        "receipt",
        "change my",
        "change it to",
        "already have tickets",
        "existing booking",
        "my booking is",
        "on my booking",
        "i booked",
        "confirmed booking",
        "meeting point for booked",
        "change participant count",
        "booking status",
        "my tickets confirmed"
        ]

    # check for the keywords in the email_content and returning the corresoponding label.
    if any(keyword in email_content for keyword in confirmation_keywords):
        return ["confirmation"]

    elif any(keyword in email_content for keyword in booking_inquiry_keywords):
        return ["booking_inquiry"]

    elif any(keyword in email_content for keyword in booking_follow_up_keywords):
        return ["booking_follow_up"]

    else:
        return ["unrelated"]