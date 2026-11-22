import pytest
import src.classifier as classifier

@pytest.mark.parametrize(
    "subject, body, expected",
    [
        ("I confirm my booking", "I would like to confirm my booking for the event.", ["confirmation"]),
        ("Availability inquiry", "I would like to know the availability and price for the event.", ["booking_inquiry"]),
        ("Reschedule request", "I need to reschedule my booking for the event.", ["booking_follow_up"]),
        ("Unrelated email", "This email is not related to any booking or confirmation.", ["unrelated"]),
        ("confirmation matches", "I confirm my booking and I would like to know the availability and price for the event.", ["confirmation","booking_inquiry"]),
    ]
)

def test_classify_email(subject, body, expected):
    assert set(classifier.classify_email(subject, body)) == set(expected) #Converted to set to ignore the order of the labels in the list


@pytest.mark.parametrize(
"subject, body, expected", 
    [
        ("", "", ["unrelated"]),
        ("RESCHEDULE MY BOOKING", "", ["booking_follow_up"]),
        ("", "I confirm my reservation", ["confirmation"]),
        ("Hello", "Just saying hi!", ["unrelated"]),
    ]
)

def test_classify_email_edge_cases(subject, body, expected):
    assert set(classifier.classify_email(subject, body)) == set(expected)