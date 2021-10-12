

def calculate_corpus(sip_amount, inflation_rate, roi, num_months):
    return sip_amount * ( ( ( (1 + roi) ** num_months ) - 1 ) / roi ) * ( 1 + roi )


if __name__ == '__main__':
    sip_amount = float(input('enter sip amount: '))
    inflation_rate = 6.0
    cagr = 0.12
    roi = cagr / 12
    num_months = 12 * int(input('enter the time period in years: '))

    corpus = calculate_corpus(sip_amount, inflation_rate, roi, num_months)

    print(corpus)