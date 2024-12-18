<details><!-- components dropdown -->
<summary style="color: #4ec9b0; cursor: pointer;">components</summary>

<!-- name_parts dropdown -->
<details style="margin-left: 2em; font-family: sans-serif;">
  <summary style="color: #4ec9b0; cursor: pointer;">name_parts</summary>
  <p>Three lists full of parts of names. AI generated</p>
  <details style="margin-left: 2em; font-family: sans-serif;">
    <summary style="color: #36a8ed; cursor: pointer;">name_start_parts</summary>
    <p>
      Type: list<br>
      A list containing small strings, supposed to contain typical starting parts of a name.
    </p>
  </details>
  <details style="margin-left: 2em; font-family: sans-serif;">
    <summary style="color: #36a8ed; cursor: pointer;">name_middle_parts</summary>
    <p>
      Type: list<br>
      A list containing small strings, supposed to contain typical middle parts of a name.
    </p>
  </details>
  <details style="margin-left: 2em; font-family: sans-serif;">
    <summary style="color: #36a8ed; cursor: pointer;">name_end_parts</summary>
    <p>
      Type: list<br>
      A list containing small strings, supposed to contain typical ending parts of a name.
    </p>
  </details>
</details> <!-- end of name_parts dropdown -->

<!-- race dropdown -->
<details style="margin-left: 2em; font-family: sans-serif;">
  <summary style="color: #4ec9b0; cursor: pointer;">race</summary>
<pre><code class="language-python"><span style="color: #4ec9b0;">race</span>(<span style="color: #36a8ed;">name</span>: <span style="color: #4ec9b0;">str</span>, <span style="color: #36a8ed;">strength_modifier</span>: <span style="color: #4ec9b0;">int</span>, <span style="color: #36a8ed;">constitution_modifier</span>: <span style="color: #4ec9b0;">int</span>, <span style="color: #36a8ed;">intelligence_modifier</span>: <span style="color: #4ec9b0;">int</span>, <span style="color: #36a8ed;">agility_modifier</span>: <span style="color: #4ec9b0;">int</span>)
</code></pre>
</details> <!-- end of race dropdown -->

<!-- profession dropdown -->
<details style="margin-left: 2em; font-family: sans-serif;">
  <summary style="color: #4ec9b0; cursor: pointer;">profession</summary>
<pre><code class="language-python"><span style="color: #4ec9b0;">profession</span>(<span style="color: #36a8ed;">name</span>: <span style="color: #4ec9b0;">str</span>)
</code></pre>
</details> <!-- end of profession dropdown -->

<!-- character dropdown -->
<details style="margin-left: 2em; font-family: sans-serif;">
  <summary style="color: #4ec9b0; cursor: pointer;">character</summary>
<!-- start of character setup code -->
<pre><code><span style="color: #4ec9b0;">character</span>(<span style="color: #36a8ed;">race</span>:<span style="color: #4ec9b0;">race</span>,<span style="color: #36a8ed;">profession</span>:<span style="color: #4ec9b0;">profession</span>,<span style="color: #36a8ed;">name</span>:<span style="color: #4ec9b0;">str</span>,<span style="color: #36a8ed;">initiative</span> = <span style="color: #4ec9b0;">0</span>,<span style="color: #36a8ed;">strength</span> = <span style="color: #4ec9b0;">10</span>,<span style="color: #36a8ed;">constitution</span> = <span style="color: #4ec9b0;">10</span>,<span style="color: #36a8ed;">intelligence</span> = <span style="color: #4ec9b0;">10</span>,<span style="color: #36a8ed;">agility</span> = <span style="color: #4ec9b0;">10</span>,<span style="color: #36a8ed;">armor_class</span> = <span style="color: #4ec9b0;">4</span>,<span style="color: #36a8ed;">max_health</span>=<span style="color: #4ec9b0;">10</span>)</code></pre> 
Example
  <pre><code class="language-python"><span style="color: #36a8ed;">commoner</span> = <span style="color: #4ec9b0;">profession</span>(<span style="color: #ce9151;">"commoner"</span>)
<span style="color: #36a8ed;">human</span> = <span style="color: #4ec9b0;">race</span>(<span style="color: #ce9151;">"Human"</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>)
<span style="color: #36a8ed;">player</span> = <span style="color: #4ec9b0;">character</span>(<span style="color: #36a8ed;">human</span>,<span style="color: #36a8ed;">commoner</span>,<span style="color: #d5c971;">genname()</span>)</code></pre>
<!-- end of character setup code -->

<!-- start of create_random dropdown -->
<details style="margin-left: 2em; font-family: sans-serif;">
  <summary style="color: #d5c971; cursor: pointer;">create_random()</summary> 
  Randomizes character stats
  <pre><code class="language-python"><span style="color: #d5c971;">create_random</span>(<span style="color: #36a8ed;">self</span>)</code></pre>
  Example
  <pre><code class="language-python"><span style="color: #36a8ed;">commoner</span> = <span style="color: #4ec9b0;">profession</span>(<span style="color: #ce9151;">"commoner"</span>)
<span style="color: #36a8ed;">human</span> = <span style="color: #4ec9b0;">race</span>(<span style="color: #ce9151;">"Human"</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>)
<span style="color: #36a8ed;">player</span> = <span style="color: #4ec9b0;">character</span>(<span style="color: #36a8ed;">human</span>,<span style="color: #36a8ed;">commoner</span>,<span style="color: #d5c971;">genname()</span>)
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">create_random()</span></code></pre>
</details><!-- end of create_random dropdown -->

<!-- start of printstats dropdown -->
<details style="margin-left: 2em; font-family: sans-serif;">
  <summary style="color: #d5c971; cursor: pointer;">printstats()</summary> 
  Displays character stats
  <pre><code class="language-python"><span style="color: #d5c971;">printstats</span>(<span style="color: #36a8ed;">self</span>)</code></pre>
  Example
  <pre><code class="language-python"><span style="color: #36a8ed;">commoner</span> = <span style="color: #4ec9b0;">profession</span>(<span style="color: #ce9151;">"commoner"</span>)
<span style="color: #36a8ed;">human</span> = <span style="color: #4ec9b0;">race</span>(<span style="color: #ce9151;">"Human"</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>)
<span style="color: #36a8ed;">player</span> = <span style="color: #4ec9b0;">character</span>(<span style="color: #36a8ed;">human</span>,<span style="color: #36a8ed;">commoner</span>,<span style="color: #d5c971;">genname()</span>)
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">create_random()</span>
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">printstats()</span></code></pre>
</details><!-- end of printstats dropdown -->

<!-- start of printinvent dropdown -->
<details style="margin-left: 2em; font-family: sans-serif;">
  <summary style="color: #d5c971; cursor: pointer;">printinvent()</summary> 
  Displays character inventory
  <pre><code class="language-python"><span style="color: #d5c971;">printinvent</span>(<span style="color: #36a8ed;">self</span>)</code></pre>
  Example
  <pre><code class="language-python"><span style="color: #36a8ed;">commoner</span> = <span style="color: #4ec9b0;">profession</span>(<span style="color: #ce9151;">"commoner"</span>)
<span style="color: #36a8ed;">human</span> = <span style="color: #4ec9b0;">race</span>(<span style="color: #ce9151;">"Human"</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>)
<span style="color: #36a8ed;">player</span> = <span style="color: #4ec9b0;">character</span>(<span style="color: #36a8ed;">human</span>,<span style="color: #36a8ed;">commoner</span>,<span style="color: #d5c971;">genname()</span>)
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">create_random()</span>
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">printinvent()</span></code></pre>
</details><!-- end of printinvent dropdown -->

<!-- start of equip_weapon dropdown -->
<details style="margin-left: 2em; font-family: sans-serif;">
  <summary style="color: #d5c971; cursor: pointer;"><span style="color: #d5c971;">equip_weapon</span>(<span style="color: #36a8ed;">weapon</span>:<span style="color: #4ec9b0;">weapon</span>,<span style="color: #36a8ed;">from_invent</span> = <span style="color: #36a8ed;">False</span>)</summary> 
  Equips a weapon to a character weapon slot
  <pre><code class="language-python"><span style="color: #d5c971;">equip_weapon</span>(<span style="color: #36a8ed;">self</span>,<span style="color: #36a8ed;">weapon</span>:<span style="color: #4ec9b0;">weapon</span>,<span style="color: #36a8ed;">from_invent</span> = <span style="color: #36a8ed;">False</span>)</code></pre>
  <p><b>-</b> If from_invent is True, a TypeError will return shall the specefied weapon not exist in the character inventory</p>
  Example
  <pre><code class="language-python"><span style="color: #36a8ed;">commoner</span> = <span style="color: #4ec9b0;">profession</span>(<span style="color: #ce9151;">"commoner"</span>)
<span style="color: #36a8ed;">sword</span> = <span style="color: #4ec9b0;">weapon</span>(<span style="color: #ce9151;">"sword"</span>, <span style="color: #4ec9b0;">2</span>, <span style="color: #ce9151;">"a sword"</span>, <span style="color: #da70c8;">(</span><span style="color: #4ec9b0;">2</span>,<span style="color: #4ec9b0;">6</span><span style="color: #da70c8;">)</span>,<span style="color: #4ec9b0;"> 0</span>)
<span style="color: #36a8ed;">human</span> = <span style="color: #4ec9b0;">race</span>(<span style="color: #ce9151;">"Human"</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>)
<span style="color: #36a8ed;">player</span> = <span style="color: #4ec9b0;">character</span>(<span style="color: #36a8ed;">human</span>,<span style="color: #36a8ed;">commoner</span>,<span style="color: #d5c971;">genname()</span>)
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">create_random()</span>
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">equip_weapon(<span style="color: #36a8ed;">sword</span>)</span></code></pre>
</details><!-- end of equip_weapon dropdown -->

<!-- start of attack dropdown -->
<details style="margin-left: 2em; font-family: sans-serif;">
  <summary style="color: #d5c971; cursor: pointer;"><span style="color: #d5c971;">attack</span>(<span style="color: #36a8ed;">target</span>:<span style="color: #4ec9b0;">character</span>)</summary> 
  Attacks a target
  <pre><code class="language-python"><span style="color: #d5c971;">attack</span>(<span style="color: #36a8ed;">self</span>,<span style="color: #36a8ed;">target</span>:<span style="color: #4ec9b0;">character</span>)</code></pre>
  <p><b>-</b> Roll to hit, on hit, deal damamge to target based on equiped weapon and attack roll</p>
  Example
  <pre><code class="language-python"><span style="color: #36a8ed;">commoner</span> = <span style="color: #4ec9b0;">profession</span>(<span style="color: #ce9151;">"commoner"</span>)
<span style="color: #36a8ed;">sword</span> = <span style="color: #4ec9b0;">weapon</span>(<span style="color: #ce9151;">"sword"</span>, <span style="color: #4ec9b0;">2</span>, <span style="color: #ce9151;">"a sword"</span>, <span style="color: #da70c8;">(</span><span style="color: #4ec9b0;">2</span>,<span style="color: #4ec9b0;">6</span><span style="color: #da70c8;">)</span>,<span style="color: #4ec9b0;"> 0</span>)
<span style="color: #36a8ed;">human</span> = <span style="color: #4ec9b0;">race</span>(<span style="color: #ce9151;">"Human"</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>)<br>
<span style="color: #36a8ed;">enemy</span> = <span style="color: #4ec9b0;">character</span>(<span style="color: #36a8ed;">human</span>,<span style="color: #36a8ed;">commoner</span>,<span style="color: #d5c971;">genname()</span>)
<span style="color: #36a8ed;">enemy</span>.<span style="color: #d5c971;">create_random()</span><br>
<span style="color: #36a8ed;">player</span> = <span style="color: #4ec9b0;">character</span>(<span style="color: #36a8ed;">human</span>,<span style="color: #36a8ed;">commoner</span>,<span style="color: #d5c971;">genname()</span>)
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">create_random()</span>
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">equip_weapon(<span style="color: #36a8ed;">sword</span>)</span>
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">attack(<span style="color: #36a8ed;">enemy</span>)</span></code></pre>
</details><!-- end of attack dropdown -->

<!-- start of aquire dropdown -->
<details style="margin-left: 2em; font-family: sans-serif;">
  <summary style="color: #d5c971; cursor: pointer;"><span style="color: #d5c971;">aquire</span>(<span style="color: #36a8ed;">target</span>:<span style="color: #4ec9b0;">any</span>)</summary> 
  Places an item in the character inventory
  <pre><code class="language-python"><span style="color: #d5c971;">aquire</span>(<span style="color: #36a8ed;">self</span>,<span style="color: #36a8ed;">target</span>:<span style="color: #4ec9b0;">any</span>)</code></pre>
  <p><b>-</b> The target must have the is_pickable attribute set to True or else a TypeError is raised</p>
  Example
  <pre><code class="language-python"><span style="color: #36a8ed;">commoner</span> = <span style="color: #4ec9b0;">profession</span>(<span style="color: #ce9151;">"commoner"</span>)
<span style="color: #36a8ed;">bread</span> = <span style="color: #4ec9b0;">food</span>(<span style="color: #ce9151;">"Bread"</span>, <span style="color: #4ec9b0;">0.2</span>, <span style="color: #ce9151;">"It's bread"</span></span>,<span style="color: #4ec9b0;"> 2</span>)
<span style="color: #36a8ed;">human</span> = <span style="color: #4ec9b0;">race</span>(<span style="color: #ce9151;">"Human"</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>, <span style="color: #4ec9b0;">0</span>)
<span style="color: #36a8ed;">player</span> = <span style="color: #4ec9b0;">character</span>(<span style="color: #36a8ed;">human</span>,<span style="color: #36a8ed;">commoner</span>,<span style="color: #d5c971;">genname()</span>)
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">create_random()</span>
<span style="color: #36a8ed;">player</span>.<span style="color: #d5c971;">aquire(<span style="color: #36a8ed;">bread</span>)</span></code></pre>
</details><!-- end of equip_weapon dropdown -->
</details> <!-- end of character dropdown -->
</details><!-- end of components dropdown -->

<details>
  <summary>basics</summary>
  
  ### Item 1
  Some content for item 1.
  
  ### Item 2
  Some content for item 2.
  
  ### Item 3
  Some content for item 3.

</details>
<details>
  <summary>generators</summary>
  
  ### Item 1
  Some content for item 1.
  
  ### Item 2
  Some content for item 2.
  
  ### Item 3
  Some content for item 3.

</details>
<details>
  <summary>items</summary>
  
  ### Item 1
  Some content for item 1.
  
  ### Item 2
  Some content for item 2.
  
  ### Item 3
  Some content for item 3.

</details>
<details>
  <summary>errors</summary>
  
  ### Item 1
  Some content for item 1.
  
  ### Item 2
  Some content for item 2.
  
  ### Item 3
  Some content for item 3.

</details>