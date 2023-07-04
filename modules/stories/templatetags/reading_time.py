from django import template

register = template.Library()

WORD_PER_MINUTE = 200


@register.filter()
def calculate_time(input):
    words = len(input.split())
    minutes = words // WORD_PER_MINUTE
    minutes_label = "minute" if minutes == 1 else "minutes"
    return minutes, minutes_label


@register.filter()
def reading_time_as_i(input):
    minutes, minutes_label = calculate_time(input)
    return f"{minutes} {minutes_label}" if minutes > 0 else "Less than 1 minute"


@register.filter()
def reading_time_as_s(input):
    minutes, minutes_label = calculate_time(input)

    minutes_s = (
        str(minutes)
        if minutes not in range(2, 10)
        else ["two", "three", "four", "five", "six", "seven", "eight", "nine"][
            minutes - 2
        ]
    )

    return f"{minutes_s} {minutes_label}" if minutes > 0 else "Less than one minute"
