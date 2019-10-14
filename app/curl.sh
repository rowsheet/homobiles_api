: '
curl localhost:5201/v1/charges \
    -u sk_test_4eC39HqLyjWDarjtT1zdp7dc:something \
    -d amount=2000 \
    -d currency=usd \
    -d source=tok_amex \
    -d description="Charge for jenny.rosen@example.com"
'

: '
curl localhost:5201/v1/charges \
    -X POST \
    -u sk_test_4eC39HqLyjWDarjtT1zdp7dc:something
'

: '
curl localhost:5201/v1/charges \
    -u sk_test_4eC39HqLyjWDarjtT1zdp7dc:something \
    -d recaptcha_token=abcedef \
    -d amount=2000 \
    -d currency=usd \
    -d source=tok_amex \
    -d description="Charge for jenny.rosen@example.com"
'

curl http://localhost:5201/v1/charges \
    -X POST \
    -d amount="asdfasdf" \
    -d currency="all" \
    -d source="asdfasdf" \
    -d description="asdfasdf" \
