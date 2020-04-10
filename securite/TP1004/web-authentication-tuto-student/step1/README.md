# Authentification Web

## 1. Preambule

Dans le cadre du module de scécurité, les RFC concernant la sécurité des authentifications web ont été présentées.
Dans ce TP vous serez amener à mettre en oeuvre des Authentificaiton Basic, Digest et générer des tokens signés

## 2.  Outils mis à disposition:
- Serveur Web Flask
- Outil Postman
- Un exemple de serveur Web Flask (ajout d'utilisateur, endpoints a compléter)
- Des examples de requètes Postman

## 3. Mise en oeuvre d'une authentification Basic/Digest
## 3.1 Ajout d'utilisateur dans la base
  - A l'aide du endpoint ```127.0.0.1:5000/user/add``` ajouter un utilisateur dans la base de données (Dans un premier temps le mot de 
  passe sera stocké en clair dans la BD).
  Le format de la requète devra respecter le format suivant:
    - URL: ```http://127.0.0.1:5000/user/add```
    - METHOD: ```POST```
    - BODY:
      - type: ```form-data```
      - value:
      ```
      KEY       VALUE
      username  jdoe
      password  jdoepwd
      ```

  


## 3.2 Réalisation d'une authentification Basic

  ### 3.2.1 Objectif 
  En s'appuyant sur les informations données en cours et la RFC 2617, mettez en oeuvre une authentification Basic entre Postman et le serveur Flask (endpoint ```127.0.0.1:5000/authcustom/authbasic``` )
    - Tester vos modifications à l'aide de [Postman](https://www.postman.com/downloads/)
    - Modifier le champ ```Authorization``` dans Postman

Le format de la requète devra respecter le format suivant:

  - URL: ```http://127.0.0.1:5000/authcustom/authbasic```
  - METHOD: ```POST```
  - Header:
    - ```Authorization``` field
    - type: ```Basic Auth```
      - username: jdoe
      - password: jdoepwd
  ### 3.2.2 Tips
  - Les modifications devront être réalisées dans le fichier ```./route/authCustom.py``` dans la méthode ```def authBasic():```
  - Utiliser la méthode ```def checkCredential(username, password):``` pour vérifier les crédentials reçus.
  - Utiliser la méthode ```base64``` (ref https://docs.python.org/3.5/library/base64.html) pour décoder du Base64 e.g :
  ```python
dataToEncode = "this is my message to encode"
encodedData = base64.b64encode(dataToEncode)

# Attention la valeur retournée est en byte
data = base64.b64decode(encodedData)

# Afin d'avoir la valeur en String il faut le décoder en utf8
print("my message:" +str(data.decode("utf-8")))
  ```

## 3.3 Réalisation d'une authentification Digest

### 3.3.1 Objectif

En s'appuyant sur les informations données en cours et la RFC 2617 mettez en oeuvre une authentification Digest entre Postman et le serveur Flask(endpoint ```http://127.0.0.1:5000/authcustom/authdigest``` )
  - Tester vos modifications à l'aide de [Postman](https://www.postman.com/downloads/)
  - Modifier le champ ```Authorization``` dans Postman

Le format de la requète devra respecter le format suivant:

  - URL: ```http://127.0.0.1:5000/authcustom/authdigest```
  - METHOD: ```POST```
  - Header:
    - ```Authorization``` field
    - type: ```Digest Auth```
      - username: ```jdoe```
      - password: ```jdoepwd```
      - Realm: ```myAuthWorld```
      - Nonce: ```dcd98b7102dd2f0e8b11d0f600bfb0c093```
      - Algorithm: ```MD5```
    - les champs suivants seront laissés vides:
      - qop
      - Nonce Count
      - Client Nonce
      - Opaque


### 3.3.2 Tips
- Les modifications devront être réalisées :
  - dans le fichier ```./route/authCustom.py``` dans la méthode ```def authDigest():```
  - dans le fichier ```./tools/CipherTools.py``` dans la méthode ```def computeHashDIgest
  ():``` (utilitaire à utiliser dans ```def authDigest():```)
      
- Utiliser la suite d'utilitaires ```hashlib``` (ref https://docs.python.org/fr/3/library/hashlib.html) pour le protocol Digest
- Pour utiliser/créer un hash correct des chaines de caractères, il faut convertir en ```utf-8``` ces dernières:

    ```python 
        ...
        data_stringA = "myDataA"
        data_stringB = "myDataB"
        hash_tool = hashlib.sha512()
        hash_tool.update(data_stringA.encode('utf-8'))
        hash_tool.update(data_stringB.encode('utf-8'))

        result = hash_tool.hexdigest()
        print(str(result))
        ...
    ```


  ## 4 Management de token d'authentification
  ### 4.1 Génération d'un token d'authentification

  #### 4.1.1 Objectif
  En cas de success de l'authentification le serveur devra ajouter un token signé dans les cookies (e.g à la fin de ```def authDigest():``` et ```def authDigestBasic```).

  Pour ce faire le token généré sera composé de:
    
  - ```Username```
  - ```Date``` de la création du token (time elapsed since epoch)
  - Identifiant unique ```UUID``` (uuid pour plus d'info voir ici https://docs.python.org/2/library/uuid.html)
  - La signature du token 
    -   la signature du token aura la forme suivante:
    ```JSON
    SHA256(
      {"username":"jdoe","time":1583155450.587793,"uuid":"a8098c1a-f86e-11da-bd1a-00112444be1e", "secret":"myVerySecret"})
    ```
  #### 4.1.2 Tips
  - Les modifications devront être réalisées :
    - dans le fichier ```./route/authCustom.py``` dans les méthodes ```def authDigest():``` et ```def authDigestBasic():```
    - dans le fichier ```./tools/CipherTools.py``` dans la méthode ```def generateTokenSHA256(username,key):``` (utilitaire à utiliser dans ```def authDigest():``` et ```def authDigestBasic():```)


  - Pour modifier les cookies du web browser utiliser la méthode ci-dessous
    ```python
    token_value="this is my value for the token"
    response.set_cookie('MyToken', token_value)
    ```
  - Vous pourrez stocker le token sous forme de string en utilisant l'utilistaire ```json.dump```:

    ```python
    my_object={ "user": "jdoe", "myAtt": " a value"}
    my_object_stringyfy=json.dumps(my_object)
    print (my_object_stringyfy)
    ```
  
  ### 4.2 Validation d'un token d'authentification

  #### 4.2.1 Objectif

  Une fois l'utilisateur authentifié, il possédera un token d'authentificaiton dans ces cookies. Dès lors, pour toutes les interactions suivantes avec le serveur, le token généré sera présenté au server.
  L'objectif de cette section est de vérifier l'exactitude du token présent dans les cookies du web browser.

  Pour ce faire vous devrez vérifiez:
    
  - l'exactitude de la signature du token
  - la validité du token (date de création < seuil)

  
  
  #### 4.2.2 Tips
  - Les modifications devront être réalisées :

    - dans le fichier ./route/authCustom.py dans la méthode ```def checkT():```

    - dans le fichier ./tools/CipherTools.py dans la méthode def ```checkTokenSHA256(key,token_received):``` (utilitaire à utiliser dans ```def checkT():```)
  
  
  - Pour récupérer les valeurs des cookies du web browser utiliser la méthode 

    ```python
    token_content = request.cookies.get('MyToken')
    ```

  - Pour convertir une chaine de caractère en objet Json utiliser la méthode ```json.loads()```

    ```python
    my_obj_string = '{"attA":"A", "attB":"B", "attC":"C", "attD":"D"}'
    my_obj_json = json.loads(my_obj_string)
    print("AttA: " + str(my_obj_json["attA"]))
    print("AttB: " + str(my_obj_json["attB"]))
    ```