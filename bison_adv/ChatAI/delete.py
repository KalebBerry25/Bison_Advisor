

import pinecone

index_name = "bison-adv"
pinecone.init(api_key='3050022e-9d8b-4963-96bc-854f8062c492',environment="gcp-starter")

index = pinecone.Index(index_name)

delete_response = index.delete(delete_all=True)