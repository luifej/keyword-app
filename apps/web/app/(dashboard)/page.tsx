"use client";
import { useState } from "react";
export default function Page(){
  const [seed,setSeed]=useState(""); const [resp,setResp]=useState<any>(null);
  async function run(){
    const r = await fetch("/api/proxy", {method:"POST", body: JSON.stringify({seed, country:"US", lang:"en"})});
    setResp(await r.json());
  }
  return (<div className="p-6 max-w-3xl mx-auto">
    <h1 className="text-2xl font-bold mb-4">Keyword Finder MVP</h1>
    <input className="border p-2 mr-2" value={seed} onChange={e=>setSeed(e.target.value)} placeholder="Seed keyword" />
    <button className="px-4 py-2 bg-black text-white" onClick={run}>Discover</button>
    <pre className="mt-4 text-sm">{JSON.stringify(resp,null,2)}</pre>
  </div>);
}
