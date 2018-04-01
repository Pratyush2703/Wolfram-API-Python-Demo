import wolframalpha
client= wolframalpha.Client("<Your_App_ID_Goes_Here>")
z = "(7^3) mod 11"
res = client.query(z)
try:
    print (next(res.results).text)
except StopIteration:
    print ("No results")