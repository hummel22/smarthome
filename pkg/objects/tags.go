package objects

type Tags map[string]string

type ApiTags struct {
	Source string
	Client string
}

func NewApiTags(source, client string) *ApiTags {
	return &ApiTags{
		Source: source,
		Client: client,
	}
}

func (a ApiTags) Tags(area string) Tags {
	return Tags{
		"source": a.Source,
		"type":   "api",
		"area":   area,
		"client": a.Client,
	}
}