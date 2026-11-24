````
# hey, i'm toeesh.

[![Website](https://img.shields.io/badge/toeesh.dev-181717?style=flat-square&logo=firefoxbrowser&logoColor=white)](https://toeesh.dev)
[![MTTA](https://img.shields.io/badge/take_the_metro-181717?style=flat-square&logo=metro&logoColor=white)](https://toeeshnetwork.vercel.app)
[![GitHub](https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/toeeshchaudhary)
![Location](https://img.shields.io/badge/delhi,_india-181717?style=flat-square&logo=googlemaps&logoColor=white)

i like computers, preferably at the level where things start getting unnecessarily complicated.

most of my work lives somewhere between embedded systems, graphics programming, reverse engineering and developer tooling. i like knowing what happens underneath an abstraction just as much as i like building things with it.

sometimes that means wiring up an ESP32. sometimes it means staring at a broken Vulkan frame at 3 in the morning.

```text
location     delhi, india
interests    hardware / graphics / systems
environment  linux
status       probably debugging something
````
an experiment in how much you can measure with inexpensive hardware. an ESP32-based field-monitoring system that brings sensor readings from the physical world into a web dashboard.
an infinite canvas for handwritten things. built the ink renderer in Rust using wgpu, with pressure-sensitive strokes and R-tree spatial indexing for efficient stroke selection and erasing.

turns out getting digital ink to feel like actual ink is a rather interesting engineering problem.
independent research into Xbox-to-PC graphics compatibility and GTA VI static recompilation, alongside contributions to Leonida.

built a standalone Vulkan renderer for experimenting with decoded geometry and translated shaders. tested everything from a 17,168-triangle handguard to controlled pixel-shader inputs with measurable outputs.

broken pixels are surprisingly useful when you know what they're supposed to look like.

project

what it does

stack

[destro](https://github.com/toeeshchaudhary/destro?utm_source=chatgpt.com)

a coding-agent harness with an advisor mode for getting a second opinion without leaving the session.


[chamak](https://github.com/toeeshchaudhary/chamak?utm_source=chatgpt.com)

a rule-based Indian stock screener with a custom parser and evaluator. every score has an explanation.


[pracq](https://github.com/toeeshchaudhary/pracq?utm_source=chatgpt.com)

flashcards and practice tests in a single binary. Markdown decks, because not everything needs a database.

- authored all 16 challenges for my school's CTF, including a tiny bytecode VM for participants to reverse engineer.
- built [MTTA](https://toeeshnetwork.vercel.app?utm_source=chatgpt.com), a portfolio disguised as a functional transit network. pick a station, explore a project, get yourself a boarding pass.
- interested in resilient distributed systems, embedded computing, GPU programming and the occasional unnecessarily ambitious side project.
languages

hardware & graphics

environment & infrastructure

## Visual direction

<box border radius="lg" padding={4} gap={3} theme="dark" background="#0d1117">
  <title size="xl" color="#e6edf3">hey, i'm toeesh.</title>
  <row wrap="wrap" gap={1}>
    {#each ["◉ toeesh.dev","▣ take the metro","◈ github","⌖ delhi, india"] as item}
      <box background="#21262d" radius="sm" padding={1}><text size="xs" color="#e6edf3">{item}</text></box>
    {/each}
  </row>
  <text size="sm" color="#c9d1d9">i like computers, preferably at the level where things start getting unnecessarily complicated.</text>
  <box background="#161b22" padding={3} radius="md">
    <text preserveWhitespace={true} size="sm" color="#8b949e">location     delhi, india
interests    hardware / graphics / systems
environment  linux
status       probably debugging something</text>
  </box>
  <divider color="#30363d"/>
  <title size="lg" color="#e6edf3">01 / closer to the metal</title>
  <text color="#58a6ff" weight="medium">AEGIS ↗</text>
  <row wrap="wrap" gap={1}>
    <box background="#21262d" padding={1} radius="sm"><text size="xs" color="#e7352c">◈ ESP32</text></box>
    <box background="#21262d" padding={1} radius="sm"><text size="xs" color="#ffffff">Next.js</text></box>
    <box background="#21262d" padding={1} radius="sm"><text size="xs" color="#c9d1d9">Embedded Systems</text></box>
  </row>
  <text size="sm" color="#c9d1d9">an experiment in how much you can measure with inexpensive hardware.</text>
  <divider color="#30363d"/>
  <title size="lg" color="#e6edf3">04 / the toolbox</title>
  <row wrap="wrap" gap={2}>
    {#each [{n:"RUST",c:"#dea584"},{n:"C",c:"#a8b9cc"},{n:"GO",c:"#00add8"},{n:"PYTHON",c:"#3776ab"},{n:"TYPESCRIPT",c:"#3178c6"},{n:"VULKAN",c:"#ac162c"},{n:"ARCH LINUX",c:"#1793d1"}] as t}
      <box background="#21262d" padding={2} radius="sm"><row gap={1}><svg viewBox="0 0 10 10" width="10px" height="10px"><circle cx="5" cy="5" r="4" fill={t.c}/></svg><text size="xs" weight="medium" color="#e6edf3">{t.n}</text></row></box>
    {/each}
  </row>
  <divider color="#30363d"/>
  <title size="lg" color="#e6edf3">05 / some numbers</title>
  <grid columns={2} gap={2}>
    <grid-item>
      <box border={{size:1,color:"#30363d"}} radius="md" padding={3}>
        <text size="sm" weight="medium" color="#e6edf3">GitHub Stats</text>
        {#each ["Total Stars","Total Commits","Pull Requests","Contributions"] as s}
          <row><text size="xs" color="#8b949e">{s}</text><spacer/><text size="xs" color="#58a6ff">—</text></row>
        {/each}
      </box>
    </grid-item>
    <grid-item>
      <box border={{size:1,color:"#30363d"}} radius="md" padding={3}>
        <text size="sm" weight="medium" color="#e6edf3">Most Used Languages</text>
        <box height="10px" radius="full" clip={true} direction="row" gap={0}>
          {#each ["#dea584","#3178c6","#00add8","#3572a5","#555555"] as c}
            <box flex={1} background={c}/>
          {/each}
        </box>
        <text size="xs" color="#8b949e">Rust · TypeScript · Go · Python · C</text>
        <caption>Live data on GitHub</caption>
      </box>
    </grid-item>
  </grid>
  <text textAlign="center" size="xs" color="#8b949e">still figuring out how things work. occasionally making them work.</text>
</box>
<caption>Illustrative preview. Actual statistics populate from your GitHub account.</caption>
