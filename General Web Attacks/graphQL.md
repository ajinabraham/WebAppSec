**Basic Schema Enum**

`{"query": "{__schema{types{name}}}"}`

**Enum Query and Description**

`{"query": "{__schema{queryType{name,fields{name,description}}}}"}`

**Enum Introspection**

```
{"query": "query IntrospectionQuery{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}"}
```

**Schemas**
When you interact with GraphQL you do so through the query language. Since this query language is providing an interface to your backend data, it needs a definition of how the data and queries should be structured. This is where the schema comes in, it simply contains the information about what queries are supported. This serves as a validation layer to ensure incoming queries are well formed and supported.

**Types**
Since GraphQL provides an interface to data, it needs a type system to define the different data-types that are supported. The supported types can be found here. Essentially you are looking at things scaler types such as Int, String, Float, Boolean and ID. And a few other types, enum, lists, interfaces.

**Fields**
These are the actual data values that are available in a data Object. In any GraphQL query you will see fields, if you ask for a field, and it is defined in the schema, it will be return to you.

**Arguments**
Just like other query languages, GraphQL provides a mechanism for limiting the data that is returned. Arguments are used for this purpose and are defined in the schema. Here again GraphQL uses the schema to validate a given query, and set of arguments, before being passed to the API responsible for retrieving the relevant data. This forces strong typing and is just another mechanism that prevents injection attacks.

**Mutations**
Sometimes you don’t want to query data, you want to modify it. This is where mutations come in. Mutations allow you to define the “functions” that can be executed through GraphQL, including the fields that are modified and the arguments that are allowed.

**Introspection**
This is where GraphQL gets really interesting, even more so if you are doing a security audit. GraphQL can be used to query itself, more specifically, the introspection system allows us to retrieve the full GraphQL schema. This is another piece of well documented information, but not many web app testers seem to be aware of it.


**Source Reference**

https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection
https://staaldraad.github.io/post/2018-03-16-quick-win-with-graphql/
https://github.com/doyensec/graph-ql

**Hardening**
https://github.com/helfer/graphql-disable-introspection
https://blog.apollographql.com/securing-your-graphql-api-from-malicious-queries-16130a324a6b
