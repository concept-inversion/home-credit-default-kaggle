import time
from py2neo import Graph, Node
import networkx as nx 
graph = Graph(password = "rosebay")
query = '''
        optional match(a:Application)-[:HAS_PREVIOUS]->(p)-[:HAS_PREV_INSTALLMENTS]->(i) with
toInteger(i.DAYS_INSTALMENT)-toInteger(i.DAYS_ENTRY_PAYMENT) as DaysInstallMinusEntry,
count(i) as TotalInstallments
optional match(a)-[:HAS_BUREAU]->(bureau) with size(filter(x IN collect(bureau.CREDIT_ACTIVE) WHERE x="Active")) as TotalActiveBureau,a.SK_ID_CURR as ApplicationID,count(bureau) as TotalBureau, TotalInstallments,DaysInstallMinusEntry
return ApplicationID,TotalInstallments,DaysInstallMinusEntry,TotalBureau,
toFloat(TotalActiveBureau)/toFloat(TotalBureau) as ActiveBureauByTotalBureauRatio order by ActiveBureauByTotalBureauRatio desc
        '''
start = time.time()
data = graph.run(query)
end = time.time()
total = end - start
#import ipdb; ipdb.set_trace()
#time = timeit.Timer('data = graph.run(query)')
print(f"It took  {total} seconds to run the query")