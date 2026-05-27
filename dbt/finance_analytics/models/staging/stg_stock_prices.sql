with source as (
    select * from {{ source('default', 'transformed_stock_prices') }}
),

renamed as (
    select
        date,
        ticker,
        open,
        high,
        low,
        close,
        volume,
        daily_return_pct,
        rolling_7d_avg_close,
        rolling_7d_avg_volume,
        prev_close,
        day_of_week,
        month,
        year,
        ingested_at
    from source
)

select * from renamed