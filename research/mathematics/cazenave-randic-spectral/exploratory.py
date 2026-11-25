import numpy as np, math, random, time
rng=np.random.default_rng(42)
best=np.full(3,np.inf); witnesses=[None]*3; count=0
# blowups of a connected template. Random sparse, dense, and modular patterns
for k in range(3,13):
  for j in range(3000):
    p=rng.uniform(.12,.95); B=np.triu(rng.random((k,k))<p,1); B=(B+B.T).astype(float)
    # ensure connectivity, add path with random permutation half of cases
    perm=rng.permutation(k)
    for a,b in zip(perm[:-1],perm[1:]): B[a,b]=B[b,a]=1
    c=rng.integers(0,2,k); s=np.maximum(1,np.round(np.exp(rng.uniform(0,6,k)))).astype(int)
    d=B@s+c*(s-1)
    M=B*np.sqrt(s[:,None]*s[None,:])+np.diag(c*(s-1)); eig=np.linalg.eigvalsh(M); L,t=eig[-1],eig[-2]
    if np.any((s>1)&(c==0)): t=max(t,0.)
    if np.any((s>1)&(c==1)): t=max(t,-1.)
    m=(s@d)/2; h=s/np.sqrt(d); R=(h@B@h + np.sum(c*s*(s-1)/d))/2
    vals=np.array([R-t-1,m-L*(t+1),2*m-L*L-(t+1)**2]); count+=1
    for i,v in enumerate(vals):
      if v<best[i]: best[i]=v;witnesses[i]=(k,B.astype(int).tolist(),c.tolist(),s.tolist(),L,t,R,m);print('best',i,v,'n',sum(s),'L,t,R,m',L,t,R,m,flush=True)
    if min(vals)<-1e-6:
      print('NEG',vals,witnesses,flush=True)
      if vals[0]<-1e-6: break
  if best[0]<-1e-6:break
print('done',count,best,witnesses)
