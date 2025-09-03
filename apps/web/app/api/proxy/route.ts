export async function POST(req: Request){
  const body = await req.json();
  const r = await fetch(process.env.API_URL + "/keywords/discover", {
    method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify(body)
  });
  return new Response(await r.text(), {status:r.status});
}
