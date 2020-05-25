package io

import (
	"context"
	"google.golang.org/api/fitness/v1"
	"google.golang.org/api/option"
	"time"
)


type GoogleFitReader struct {

}


func NewGoogleFitReader(ctx context.Context, apiKey string) (*GoogleFitReader, error) {
	fitnessService, err := fitness.NewService(ctx, option.WithAPIKey(apiKey))
	if err != nil {
		return nil, err
	}

	now := time.Now()
	yesterday := now.Add(time.Hour*20 *-1)
	fitnessService.Users.DataSources.Get("id","derived:com.google.step_count.delta:com.google.android.gms:estimated_steps")
	fitnessService.Users.Dataset.Aggregate(
		"id",
		&fitness.AggregateRequest{
		AggregateBy: []*fitness.AggregateBy{
			&fitness.AggregateBy{
				DataSourceId:    "",
				DataTypeName:    "",
				ForceSendFields: nil,
				NullFields:      nil,
			},
		},
		BucketByActivitySegment:     nil,
		BucketByActivityType:        nil,
		BucketBySession:             nil,
		BucketByTime:                nil,
		EndTimeMillis:               int64(now.Second()*1000),
		StartTimeMillis:             int64(yesterday.Second()*1000),
		ForceSendFields:             nil,
		NullFields:                  nil,
	},
	)
}