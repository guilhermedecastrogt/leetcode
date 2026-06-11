function earliestFinishTime(landStartTime: number[], landDuration: number[], waterStartTime: number[], waterDuration: number[]): number {
    var minimal_time = 99999;

    for(var i = 0; i < landStartTime.length; i++){
        for(var j = 0; j < waterStartTime.length; j++){
            let land = landStartTime[i] + landDuration[i];

            let water = 0;

            if(land == waterStartTime[j]){
                water = waterStartTime[j] + waterDuration[j];;
            } else if (land > waterStartTime[j]){
                water = land + waterDuration[j];
            } else if(land < waterStartTime[j]) {
                let d = waterStartTime[j] - land;
                land = land + d;
                water = land + waterDuration[j];
            }

            console.log(water);

            if(water < minimal_time) {
                minimal_time = water;
            }


            let water2 = waterStartTime[j] + waterDuration[j];

            let land2 = 0;

            if(water2 == landStartTime[i]) {
                land2 = landStartTime[i] + landDuration[i];
            } else if(water2 > landStartTime[i]) {
                land2 = water2 + landDuration[i];
            } else if(water2 < landStartTime[i]) {
                let d2 = landStartTime[i] - water2;
                water2 = water2 + d2;
                land2 = water2 + landDuration[i];
            }

            console.log(land2);

            if(land2 < minimal_time) {
                minimal_time = land2;
            }
        }   
    }

    return minimal_time;
};