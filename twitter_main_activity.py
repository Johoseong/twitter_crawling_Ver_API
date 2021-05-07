import twitter_set_drugs
import twitter_crawling_Ver_API

drug_brand1 = twitter_set_drugs.Drugs()
main_crawling = twitter_crawling_Ver_API.Crawling()

print(drug_brand1.lists)

main_crawling.main_act()
