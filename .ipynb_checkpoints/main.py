from flask import Flask,jsonify,render_template,request
from project_app.utils import KmeanCluster
app=Flask(__name__)

@app.route("/")
def hello_flask():
    print("Welcome to Clustering prediction")
    return render_template("index.html")

@app.route("/predict cluster",methods=["POST","GET"])
def Cluster_Prediction():
    if request.method=="GET":
        print("we are in GET method")

    nsites=request.args.get("nsites")
    volume=request.args.get("volume")
    density=request.args.get("density")
    symmetry__number=request.args.get("symmetry__number")
    symmetry__symprec=request.args.get("symmetry__symprec")
    formation_energy_per_atom=request.args.get("formation_energy_per_atom")
    energy_above_hull=request.args.get("energy_above_hull")
    band_gap=request.args.get("band_gap")
    total_magnetization=request.args.get("total_magnetization")
    is_stable=request.args.get("is_stable")
    is_metal=request.args.get("is_metal")
    theoretical=request.args.get("theoretical")
    symmetry__crystal_system=request.args.get("symmetry__crystal_system")
    symmetry__symbol=request.args.get("symmetry__symbol")
    symmetry__point_group=request.args.get("symmetry__point_group")
    ordering=request.args.get("ordering")

    output= KmeanCluster(nsites,volume,density,symmetry__number,symmetry__symprec,formation_energy_per_atom,energy_above_hull,band_gap,total_magnetization,is_stable,is_metal,theoretical,symmetry__crystal_system,symmetry__symbol,symmetry__point_group,ordering)
    cluster=output.Prediction()
    return render_template("index.html", prediction = cluster)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = True)
